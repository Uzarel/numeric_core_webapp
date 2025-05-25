# Numeric Core Calculator

A lightweight Streamlit application inspired by the "Numeric Core" late-game puzzle concept from the game **Blue Prince**. This tool computes the *numeric core* of a sequence of four non-negative integers by applying a fixed leading `+` operation followed by all permutations of the operators `-`, `*`, and `/` in left‑to‑right order, selecting the smallest non-negative integer result.

---

## Features

* Reports the smallest achievable *numeric core* and the corresponding operator sequence.
* Built with Streamlit for an interactive web interface.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Uzarel/numeric_core_webapp.git
   cd numeric_core_webapp
   ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the app**

   ```bash
   streamlit run app.py
   ```

2. **Interact in the browser**

   * Enter four non-negative integers into the input fields.
   * Click **Compute** to see the resulting *numeric core* and the operator sequence.
   * If no valid core is found or the result has four or more digits, a warning will prompt for new inputs.

---

## Contributing

Contributions, bug reports, and pull requests are welcome! Feel free to open an issue or submit a PR to enhance the puzzle logic, improve the UI, or add new features.
