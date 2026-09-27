from future import annotations

import logging
from dataclasses import asdict, dataclass, field

LOGGER = logging.getLogger(name)

@dataclass(frozen=True)
class ReportSection:
  """Represents a single titled section within a report."""

heading: str
body: str

@dataclass(frozen=True)
class Report:
  """Aggregates metadata and sections for a PDF report."""

title: str
author: str
sections: list[ReportSection] = field(default_factory=list)

def to_dict(self) -> dict[str, object]:
  """Serialize the report to a JSON-friendly dictionary."""
  return {
  "title": self.title,
  "author": self.author,
  "sections": [asdict(section) for section in self.sections],
  }

def render_text(self) -> str:
  """Render a plain-text preview of the report."""
  lines = [self.title, f"By {self.author}", ""]
  for section in self.sections:
    lines.append(section.heading)
    lines.append(section.body)
    lines.append("")
    return "\n".join(lines).strip()

def build_sample_report() -> Report:
  """Create a sample report used for local demos."""
  return Report(
  title="Monthly Report",
  author="Shiv Pratap Singh",
  sections=[
  ReportSection(heading="Summary", body="All systems operational."),
  ReportSection(heading="Metrics", body="Uptime 99.9%, latency 120ms."),
  ],
  )

def main() -> int:
  """Application entry point."""
  logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

report = build_sample_report()
LOGGER.info("Rendering report: %s", report.title)
print(report.render_text())
return 0

if name == "main":
  raise SystemExit(main())
  
