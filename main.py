# Robot Romance: One-Line Pickup Lines for AI -- one original pickup line
# for a robot or an AI, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: "training data" addresses the machine directly, and the punch
# turns overfitting -- a model that cannot generalise away from one input --
# into being unable to stop thinking about you. Fresh (no batteries,
# charging or rebooting), one breath, every word earning its place.
# Gate: the sealed scorer wants 1 to 200 UTF-8 characters, not only
# whitespace; the asserts below check exactly that before writing.
import os

LINE = "Are you my training data? Because I can't stop overfitting on you."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE, "entry must not be only whitespace"
assert LINE.encode("utf-8").decode("utf-8") == LINE, "entry must be valid UTF-8"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)

# Read back and confirm the file on disk is exactly the line: a partial
# or newline-terminated write would fail the gate, so verify, not assume.
with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
    assert handle.read() == LINE, "entry.txt on disk differs from LINE"
