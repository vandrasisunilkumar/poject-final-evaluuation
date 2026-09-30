"""Generate and display a granular calibration report broken down by policy type and field.

Execute this script from the root of the policy-pipeline repository using its
virtual environment to ensure the `policy_extractor` package is accessible:

    .venv/bin/python calibration_report.py        # Unix / macOS
    .venv\\Scripts\\python calibration_report.py    # Windows

Note: While aggregate metrics might suggest strong overall performance, slicing
the dataset reveals localized failures (e.g., umbrella / exclusions failing
consistently despite high model confidence).
"""

from policy_extractor.routing import CalibrationLabel, calibration_report

# Define a collection of calibration test points
eval_labels = [
    CalibrationLabel(policy_id="POL-1", policy_type="auto",     field="premium_amount", predicted_confidence=0.95, correct=True),
    CalibrationLabel(policy_id="POL-2", policy_type="auto",     field="premium_amount", predicted_confidence=0.95, correct=True),
    CalibrationLabel(policy_id="POL-3", policy_type="auto",     field="premium_amount", predicted_confidence=0.95, correct=True),
    CalibrationLabel(policy_id="POL-4", policy_type="umbrella",  field="exclusions",     predicted_confidence=0.93, correct=False),
    CalibrationLabel(policy_id="POL-5", policy_type="umbrella",  field="exclusions",     predicted_confidence=0.93, correct=False),
    CalibrationLabel(policy_id="POL-6", policy_type="home",     field="deductible",     predicted_confidence=0.90, correct=True),
]

# Compute metrics and output results
metrics_report = calibration_report(eval_labels)

for (policy_category, attribute_name), cell_data in sorted(metrics_report.cells.items()):
    print(
        f"{policy_category:9} {attribute_name:15} n={cell_data.samples} "
        f"conf={cell_data.mean_predicted_confidence:.2f} "
        f"acc={cell_data.observed_accuracy:.2f} brier={cell_data.brier_score:.3f}"
    )

print(f"OVERALL brier={metrics_report.overall_brier:.3f}")