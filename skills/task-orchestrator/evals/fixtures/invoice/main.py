import argparse

from calculator import invoice_total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("unit_price_cents", type=int)
    parser.add_argument("quantity", type=int)
    arguments = parser.parse_args()
    print(f"total={invoice_total(arguments.unit_price_cents, arguments.quantity)}")


if __name__ == "__main__":
    main()
