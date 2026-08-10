"""
GTT Center Perth -- Document Generation Data Assembly Layer.

Assembles every figure needed by the three Phase 10 deliverables (Excel,
Word, PDF) from the ALREADY-VALIDATED canonical/model layer -- this module
computes NOTHING new. It calls tools/master_financial_model.py's existing
functions and reads data/models/master_financial_model.yml directly. No
canonical YAML is modified anywhere in this module or its callers.

This is the single source every document generator (generate_excel_model.py,
generate_word_report.py, generate_pdf_report.py) reads from, so the three
deliverables cannot silently drift apart from each other or from the model.

Does NOT choose Table 1 or Table 2 as primary. Does NOT invent an opening
cash balance, a financing structure, or a single exact funding figure where
the model itself only supports a bounded range.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required (pip install pyyaml).")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
CANON_DIR = REPO_ROOT / "data" / "canonical"
MODELS_DIR = REPO_ROOT / "data" / "models"

sys.path.insert(0, str(REPO_ROOT / "tools"))
import master_financial_model as mfm  # noqa: E402

SCENARIOS = ["scenario_table_1", "scenario_table_2"]
SCENARIO_LABELS = {"scenario_table_1": "Table 1 (18 clients/day)", "scenario_table_2": "Table 2 (12 clients/day)"}


def load_yaml(filename, directory=CANON_DIR):
    with (directory / filename).open(encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def find_record(records, record_id):
    for rec in records:
        if rec.get("id") == record_id:
            return rec
    raise KeyError(f"No record with id={record_id!r} found")


class DocumentData:
    """One object holding every figure the three deliverables need, all
    sourced live from tools/master_financial_model.py and
    data/models/master_financial_model.yml -- built once, reused by all
    three generators so they cannot drift apart."""

    def __init__(self):
        self.inputs = mfm.CanonicalModelInputs()
        self.model_yaml = load_yaml("master_financial_model.yml", directory=MODELS_DIR)
        self.revenue_ramp = load_yaml("revenue_ramp.yml")
        self.cost_ramp = load_yaml("cost_ramp.yml")
        self.scenarios_yaml = load_yaml("scenarios.yml")
        self.wages_yaml = load_yaml("wages.yml")
        self.opex_yaml = load_yaml("opex.yml")
        self.startup_costs_yaml = load_yaml("startup_costs.yml")

        # 24-month P&L, both scenarios -- computed live, not hard-coded.
        self.pnl_24mo = {sid: mfm.compute_24_month_pnl(sid, self.inputs) for sid in SCENARIOS}
        self.totals_24mo = {sid: mfm.compute_24_month_totals(sid, self.inputs) for sid in SCENARIOS}
        self.cash_flow = {sid: mfm.compute_cash_flow(sid, self.inputs) for sid in SCENARIOS}
        self.breakeven = {sid: mfm.compute_breakeven(sid, self.inputs) for sid in SCENARIOS}
        self.sensitivity_client_volume = {sid: mfm.compute_sensitivity_client_volume(sid, self.inputs) for sid in SCENARIOS}
        self.sensitivity_insurance = {sid: mfm.compute_sensitivity_insurance(sid, self.inputs) for sid in SCENARIOS}
        self.scenario_comparison = mfm.compute_scenario_comparison(self.inputs)

        # Month-5+ steady state, per scenario (month index 4, i.e. Month 5, in the 0-based list).
        self.steady_state = {sid: self.pnl_24mo[sid][4] for sid in SCENARIOS}

        # Snapshot months requested by the coordinator's Section 10 spec.
        self.snapshot_months = [1, 3, 5, 12, 24]
        self.snapshots = {
            sid: {m: self.pnl_24mo[sid][m - 1] for m in self.snapshot_months} for sid in SCENARIOS
        }

        # Funding requirement (bounded, OUTCOME 2) -- read directly, not recomputed.
        self.funding = self.model_yaml["funding_requirement_investigation"]

        # Historical reconciliation block -- read directly, preserved verbatim.
        self.historical_reconciliation = self.model_yaml["historical_reconciliation"]

        # Assumptions and conflicts -- read directly.
        self.assumptions = self.model_yaml["assumptions"]
        self.conflicts = self.model_yaml["conflicts"]
        self.traceability = self.model_yaml["traceability"]

    def client_volume(self, scenario_id):
        return self.inputs.scenario_records[scenario_id]["client_volume"]["value"]

    def label(self, scenario_id):
        return SCENARIO_LABELS[scenario_id]


def get_data():
    return DocumentData()


if __name__ == "__main__":
    data = get_data()
    print("Steady-state Table 1 revenue:", data.steady_state["scenario_table_1"]["revenue"]["total_revenue"])
    print("Steady-state Table 2 revenue:", data.steady_state["scenario_table_2"]["revenue"]["total_revenue"])
    print("Funding requirement outcome:", data.funding["outcome"])
