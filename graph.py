from langgraph.graph import StateGraph, END
from agents.data_collector import data_collector_agent
from agents.anomaly_detector import anomaly_detector_agent
from agents.report_writer import report_writer_agent
from typing import TypedDict, Any

# --- Define the shared state structure ---
class ReportState(TypedDict):
    ga4_property_id: str
    gsc_site_url: str
    client_name: str
    ga4_data: Any
    gsc_data: Any
    ads_data: Any
    anomalies: Any
    insights: Any
    report_text: str
    report_file: str

# --- Build the graph ---
def build_graph():
    graph = StateGraph(ReportState)

    # Add the three agents as nodes
    graph.add_node("data_collector", data_collector_agent)
    graph.add_node("anomaly_detector", anomaly_detector_agent)
    graph.add_node("report_writer", report_writer_agent)

    # Wire them in sequence
    graph.set_entry_point("data_collector")
    graph.add_edge("data_collector", "anomaly_detector")
    graph.add_edge("anomaly_detector", "report_writer")
    graph.add_edge("report_writer", END)

    return graph.compile()