"""
Script for documenting the Landscape Model Tarn-et-Garonne scenario.
"""
import os
import base.documentation

scenario_name = "Tarn-et-Garonne"
root_folder = os.path.abspath(os.path.join(os.path.dirname(base.__file__), ".."))
base.documentation.document_scenario(
    os.path.join(root_folder, "..", "..", "scenario", scenario_name, "scenario.xproject"),
    os.path.join(root_folder, "..", "..", "scenario", scenario_name, "README.md")
)
base.documentation.write_scenario_changelog(
    os.path.join(root_folder, "..", "..", "scenario", scenario_name, "scenario.xproject"),
    os.path.join(root_folder, "..", "..", "scenario", scenario_name, "CHANGELOG.md")
)
base.documentation.write_contribution_notes(
    os.path.join(root_folder, "..", "..", "scenario", scenario_name, "CONTRIBUTING.md"))
