import itertools
import streamlit as st
from typing import List

def numeric_core(parts: List[int]):
    """
    Given a list of four non-negative integers, compute the smallest
    non-negative integer of applying the operators '+', '-', '*', '/'
    (starting with '+') in left-to-right order, trying all permutations
    of the remaining three operators.
    """
    if len(parts) != 4:
        raise ValueError("Exactly four integers must be provided.")
    if any(p < 0 for p in parts):
        raise ValueError("All integers must be non-negative.")

    minimum = None
    # The first operator is implicitly '+' so start with parts[1]
    for ops in itertools.permutations(['-', '*', '/'], 3):
        core = parts[0]
        div0 = False
        for part, op in zip(parts[1:], ops):
            if op == '-':
                core = core - part
            elif op == '*':
                core = core * part
            elif op == '/':
                if part == 0:
                    div0 = True
                    break
                core = core / part
        # Skip division by zero
        if div0:
            continue
        # Ignore non-integer core
        if abs(core - round(core)) > 1e-9:
            continue
        core = int(round(core))
        # Ignore negative core
        if core < 0:
            continue
        if minimum is None or core < minimum:
            minimum = core
            best_ops = ops
    return minimum, best_ops if minimum is not None else None


def main():
    st.set_page_config(
        page_title="Blue Prince - Numeric Core Calculator",
        page_icon=":large_blue_circle:",
    )
    st.image("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1569580/header.jpg")
    st.title("Numeric Core Calculator")
    st.markdown(
        "Enter four positive integers below and click **Compute** to find the corresponding numeric core."
    )

    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("First integer", value=8, step=1, format="%d")
        c = st.number_input("Third integer", value=45, step=1, format="%d")
    with col2:
        b = st.number_input("Second integer", value=6, step=1, format="%d")
        d = st.number_input("Fourth integer", value=5, step=1, format="%d")

    if st.button("Compute"):
        try:
            parts = [int(a), int(b), int(c), int(d)]
            core, ops = numeric_core(parts)

            if core is None:
                st.warning("No valid numeric core found for the given inputs.")
            elif core >= 1000:
                st.warning(
                    f"The numeric core is {core}, which has four or more digits. "
                    "Please enter a new set of four integers."
                )
            else:
                st.success(f"**Numeric core**: {core}, **operations**: (+, {', '.join(ops)})")

        except Exception as e:
            st.error(f"Error: {e}")


if __name__ == "__main__":
    main()
