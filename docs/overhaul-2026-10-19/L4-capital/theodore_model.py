"""Theodore R9 model: one GST-inclusive journey, loan-first repayment, dividend streaming, Clinic 2 retention.
All inputs from gtt-center-perth repo (GST-SPLIT-MODEL.md, MODEL-WORKINGS.md). No new calculators for the business P&L;
this only layers the owners' loan/tax mechanics on the repo's after-GST monthly profit."""
import json
AM_GST_FULL=10771.36; PM_GST=2235.04; ITC=1262.58
BEFORE_GST_STEADY=35186.40          # repo operating profit, GST-inclusive, no GST line
AM_REV_INCL=118485.00               # AM package revenue per month (GST-inclusive)
def after_gst(before, c):           # c = AM capacity share
    return before - (AM_GST_FULL*c + PM_GST - ITC)
STEADY=after_gst(BEFORE_GST_STEADY,1.0)
assert abs(STEADY-23442.58)<0.01, STEADY
def path(kind, n=36):
    if kind=="steady": return [STEADY]*n
    if kind=="ramp":
        b=[-16573.03,7782.51,19292.48,30021.77]; c=[.43,.64,.79,.93]
        return [after_gst(b[i],c[i]) for i in range(4)]+[STEADY]*(n-4)
    if kind=="stress85":   # AM volume 15% below plan, costs fixed
        b=BEFORE_GST_STEADY-0.15*AM_REV_INCL
        return [after_gst(b,0.85)]*n
def repay(loan, kind, buffer=85000.0, capex_prelaunch=251198.0, n=36):
    cash=loan-(capex_prelaunch-85000.0)   # base case opens with A$85,000 cash
    bal=loan; cum=0.0; rows=[]; prev_gst=0.0; clear=None
    P=path(kind,n)
    for m,p in enumerate(P,1):
        cum+=p
        taxres=0.25*max(0.0,cum)          # tax set aside, never lent back
        cash+=p
        gst_res=max(0.0,prev_gst)
        avail=max(0.0,cash-buffer-taxres-gst_res)
        r=min(bal,avail); bal-=r; cash-=r
        rows.append(dict(m=m,profit=round(p,2),repaid=round(r,2),balance=round(bal,2),cash=round(cash,2),taxres=round(taxres,2)))
        if bal<=0.005 and clear is None: clear=m
        prev_gst=0.0
    return clear, rows
res={}
for loan in (251198.0,300000.0,336000.0):
    for kind in ("steady","ramp","stress85"):
        c,rows=repay(loan,kind)
        res[f"{int(loan)}-{kind}"]=dict(clear_month=c,rows=rows[:24])
# personal tax FY2026-27 resident, Medicare levy per person
def tax_base(x):
    t=0
    br=[(18200,0),(45000,.15),(135000,.30),(190000,.37),(1e18,.45)]
    prev=0
    for lim,r in br:
        if x>prev: t+=(min(x,lim)-prev)*r
        prev=lim
    return t
def person(other,div_cash,levy):
    gross=div_cash/0.75; cr=gross-div_cash
    taxable=other+gross
    tx=tax_base(taxable)+levy*taxable
    return gross,cr,tx, div_cash+cr-tx  # net cash to person from dividend: cash + refund/(payment) = cash+cr-tx_on_dividend part
def family(da,dp,p_other=100000.0):
    # net cash from dividends after personal tax (incremental over other income)
    a_t=tax_base(da/0.75)+0.0
    a_net=da - (a_t-da/0.75*0.25)
    b_base=tax_base(p_other)+0.02*p_other
    b_t=tax_base(p_other+dp/0.75)+0.02*(p_other+dp/0.75)-b_base
    b_net=dp-(b_t-dp/0.75*0.25)
    return a_net,b_net
def best_split(X,p_other=100000.0,step=500.0):
    best=None;d=0.0
    while d<=X+1e-9:
        a,b=family(d,X-d,p_other)
        if best is None or a+b>best[0]: best=(a+b,d,X-d,a,b)
        d+=step
    return best
AFTER_TAX=STEADY*12*0.75
tab=[]
for X in (0,50000,100000,127500,150000,AFTER_TAX):
    if X==0: tab.append(dict(cash_div=0,anthony=0,partner=0,family_net=0,retained=round(AFTER_TAX,2),eff_tax=0.25)); continue
    tot,da,dp,a,b=best_split(X)
    gross=X/0.75
    eff=1-(tot+(AFTER_TAX-X))/ (STEADY*12)  # not used
    total_tax=(STEADY*12 - (tot + (AFTER_TAX-X)))  # tax on distributed profit: pre-tax profit minus family net minus retained-after-company-tax
    # effective tax rate on the distributed slice of pre-tax profit
    slice_pre=X/0.75
    eff_slice=1-tot/slice_pre
    tab.append(dict(cash_div=round(X,2),anthony=round(da,2),partner=round(dp,2),a_net=round(a,2),p_net=round(b,2),family_net=round(tot,2),retained=round(AFTER_TAX-X,2),eff_tax_on_slice=round(eff_slice,4)))
# Clinic 2 accumulation
c2=[]
for X in (127500.0,100000.0,50000.0,0.0):
    keep=AFTER_TAX-X
    c2.append(dict(cash_div=X,retained_per_year=round(keep,2),yrs_300k=round(300000/keep,2),yrs_350k=round(350000/keep,2)))
out=dict(steady=round(STEADY,2),steady_year=round(STEADY*12,2),tax_year=round(STEADY*12*.25,2),after_tax_year=round(AFTER_TAX,2),dividend_table=tab,clinic2=c2,
 clear={k:v["clear_month"] for k,v in res.items()})
json.dump(dict(out=out,res=res),open("r9/theodore_results.json","w"),indent=1)
print(json.dumps(out,indent=1))
for k in ("251198-steady","251198-ramp","336000-steady","336000-ramp","251198-stress85"):
    print(k,[ (r['m'],r['repaid'],r['balance']) for r in res[k]['rows'][:24] if r['repaid']>0][:3], '...', res[k]['clear_month'])
