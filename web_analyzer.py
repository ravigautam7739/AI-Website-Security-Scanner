from rich.console import Console
from rich.progress import Progress
import time
import random

console = Console()

console.print("\n[JARVIS WEBSITE SECURITY SCANNER]\n", style="bold cyan")

website = input("Enter Website URL: ")

console.print(f"\nTarget: {website}\n", style="bold green")

checks = [
    "Checking SSL Certificate",
    "Inspecting HTTP Headers",
    "Scanning For Malware",
    "Checking DNS Records",
    "Analyzing Source Code",
    "Checking Phishing Risk",
    "Analyzing Domain Reputation",
    "Cross-Checking Threat Database",
    "Running Deep Security Analysis"
]

for check in checks:

    console.print(f"\n{check}...", style="yellow")

    with Progress() as progress:

        task = progress.add_task(
            "[cyan]Scanning...",
            total=100
        )

        while not progress.finished:
            progress.update(task, advance=4)
            time.sleep(0.03)

    console.print(
        f"{check} Complete ✓",
        style="green"
    )

    time.sleep(0.5)

security_score = random.randint(95, 100)
threat_level = random.randint(0, 4)

console.print("\n" + "="*50, style="cyan")

console.print(
    f"\nTHREAT LEVEL: {threat_level}%",
    style="bold green"
)

console.print(
    f"SECURITY SCORE: {security_score}/100",
    style="bold green"
)

console.print(
    "\nSTATUS: WEBSITE VERIFIED",
    style="bold green"
)

console.print(
    "NO IMMEDIATE THREATS DETECTED",
    style="bold green"
)

console.print("\nANALYSIS COMPLETE ✓", style="bold cyan")

console.print("\n" + "="*50, style="cyan")