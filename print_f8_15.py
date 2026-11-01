def print_models(unprinted_designs, completed_models):
    """Simulasikan pencetakan setiap desain sampai tidak ada yang tersisa."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Tampilkan semua model yang telah selesai dicetak."""
    print("\nModel berikut telah selesai dicetak:")
    for model in completed_models:
        print(model)