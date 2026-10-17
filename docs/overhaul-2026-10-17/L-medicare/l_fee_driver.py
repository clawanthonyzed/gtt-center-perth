import sys
sys.path.insert(0,"/root/gtt-L2/docs/overhaul-2026-10-16/M-model")
import m_part2 as P
print("DAYS",P.DAYS,"clients/month",18*P.DAYS)
for fee in (0,19.90,25.85,22.30):
    s=P.steady(fee=fee)
    be=P.be_search(fee=fee,policy="spaced"); beg=P.be_search(fee=fee,gst=True,policy="spaced")
    print("fee",fee,"cost/mo",round(fee*18*P.DAYS,2),"net",s["net"],"net_gst",s["net_gst"],"Y1",round(s["net"]*12,2),"BE",be,"BEgst",beg)
for price in (250,275.85,250+25.85):
    s=P.steady(fee=25.85)
    print("price",price,"BE with fee",P.be_search(fee=25.85,price=price,policy="spaced"))
print("2 phleb monthly wages", P.ph_lines(2), "with oncost", round(P.ph_lines(2)*1.137,2), "per phleb", round(P.ph_lines(1)*1.137,2))
print("1 phleb option net 9 clients", P.cost_n(9,"base2")[1])
