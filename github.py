import math
import pandas as pd


# Function with default parameter values
def generate_bigO_data(start=1, end=20):

    # Create an empty list to store the results
    rows = []

    # Repeat for each value of n
    for n in range(start, end):

        # Calculate different Big O examples
        o_1 = 1
        o_log_n = round(math.log2(n), 2)
        o_n = n
        o_n_log_n = round(n * math.log2(n), 2)
        o_n2 = n**2
        o_n3 = n**3
        o_exp = 2**n
        o_fact = math.factorial(n)

        # Add the results to the list
        rows.append(
            {
                "n": n,
                "O(1)": o_1,
                "O(log n)": (
                    f"{o_log_n:.2f}" if o_log_n != int(o_log_n) else str(int(o_log_n))
                ),
                "O(n)": o_n,
                "O(n log n)": (
                    f"{o_n_log_n:.2f}"
                    if o_n_log_n != int(o_n_log_n)
                    else str(int(o_n_log_n))
                ),
                "O(n*n)": o_n2,
                "O(n*n*n)": o_n3,
                "Exponential O(2^n)": f"{o_exp:,}",
                "Factorial O(n!)": f"{o_fact:,}",
            }
        )

    # Cconvert the list into a Pandas DataFrame..
    df = pd.DataFrame(rows)

    # Display the results as a table..
    print(df.to_markdown(index=False))


# Entry point - run the function when the script is executed
if __name__ == "__main__":
    generate_bigO_data()