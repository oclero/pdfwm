"""Example script demonstrating library usage of pdfwm."""

import shutil
from pdfwm import process_pdf

# Example 1: Basic usage with default color
print("Example 1: Basic watermark")
success, message = process_pdf(
    input_path="lorem-ipsum.pdf",
    output_path="../output/example1.pdf",
    watermark_text="DRAFT"
)
print(f"  {'✓' if success else '✗'} {message}\n")

# Example 2: Custom color (red with 50% opacity)
print("Example 2: Custom color watermark")
success, message = process_pdf(
    input_path="lorem-ipsum.pdf",
    output_path="../output/example2.pdf",
    watermark_text="CONFIDENTIAL",
    watermark_color="#FF000080"
)
print(f"  {'✓' if success else '✗'} {message}\n")

# Example 3: Overwrite mode
print("Example 3: Overwrite mode (creates temp copy)")
shutil.copy("lorem-ipsum.pdf", "../output/example3.pdf")
success, message = process_pdf(
    input_path="../output/example3.pdf",
    output_path="../output/example3.pdf",
    watermark_text="MODIFIED",
    overwrite=True
)
print(f"  {'✓' if success else '✗'} {message}")
