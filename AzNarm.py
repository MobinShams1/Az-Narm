
appetizers = [
    "سالاد فصل",
    "سوپ جو",
    "ماست و خیار",
    "زیتون پرورده"
]

main_dishes = ["چلو کباب","زرشک پلو با مرغ","قرمه سبزی","ته چین"]

def show_menu():
    print("=== منوی رستوران ===")
    print("\nپیش‌غذاها:")
    for item in appetizers:
        print(f"  - {item}")
    print("\nغذاهای اصلی:")
    for item in main_dishes:
        print(f"  - {item}")

if __name__ == "__main__":
    show_menu()
