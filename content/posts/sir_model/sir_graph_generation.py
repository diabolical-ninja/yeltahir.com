"""Script to solve SIR attack rate equation & plot it's change against R0."""

from math import exp

from numpy import arange

import pandas as pd

import plotly.graph_objs as go
import plotly.io as pio


def solve_attack_rate_eq(
    r0: float, s0: float = 1, an: float = 0.8, num_iters: int = 100, tol: float = 1e-100
) -> float:
    """Solves the Epidemic Attack Rate equation using the Newton-Raphson method.

    Args:
        r0 (float): Reproductive Ratio
        s0 (float, optional): Initial proportion suspectible to infection. Defaults to 1.
        an (float, optional): Initial attack rate guess. Defaults to 0.8.
        num_iters (int, optional): Number of iterations to trial. Defaults to 100.
        tol (float, optional): Early stopping criteria for convergence. Defaults to 1e-100.

    Returns:
        float: Estimated proportion of the population infected, ie the attack rate.
    """
    for i in range(0, num_iters):

        ai = an

        # Attack rate forumla
        fx = s0 * exp(-r0 * ai) + ai - s0

        # First derivative
        dfx = -r0 * s0 * exp(-r0 * ai) + 1

        # Update estimate for the attack rate
        an = ai - fx / dfx

        if abs(an - ai) <= tol:
            return an

    return an


# Calculate the attack rate for a range of R0 values to demonstrate the changes
R0_range = arange(0, 5, 0.05)
attack_rate_df = pd.DataFrame(
    {"R0": R0_range, "Attack Rate": [solve_attack_rate_eq(x) for x in R0_range]}
)


# Build the chart of attack rate changes against R0
data = [
    go.Scatter(
        x=attack_rate_df["R0"],
        y=attack_rate_df["Attack Rate"],
        line=dict(color="black"),
        hovertemplate="R0: %{x:.2f}" + "<br>Infected: %{y:.2f}<extra></extra>",
    ),
    go.Scatter(
        x=[0.5, 4.5],
        y=[0.75, 0.75],
        text=["No Epidemic"],
        mode="text",
        hoverinfo="none",
    ),
]


layout = go.Layout(
    shapes=[
        # 1st highlight during no epidemic
        dict(
            xref="x",
            yref="paper",
            x0="0",
            y0=0,
            x1="1",
            y1=1,
            fillcolor="Grey",
            opacity=0.5,
            layer="below",
            line_width=0,
        ),
        # 2nd highlight during epidemic
        dict(
            xref="x",
            yref="paper",
            x0="1",
            y0=0,
            x1="5",
            y1=1,
            fillcolor="Tomato",
            opacity=0.5,
            layer="below",
            line_width=0,
        ),
    ],
    yaxis_title="Proportion Infected",
    xaxis_title="Basic Reproductive Ratio, R0",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    showlegend=False,
    margin=dict(l=70, r=70, t=70, b=70),
)

# Create & export chart
fig = go.Figure(data=data, layout=layout)
pio.write_html(fig, file="epidemic_threshold.html")
