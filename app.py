import time
from taximeter import Taximeter, State

def print_menu():
    print("🚕 TaxiTech - Terminal para conductores")
    print("-" * 35)
    print("  [ I ] - Iniciar carrera")
    print("  [ M ] - En movimiento (0,05 €/s)")
    print("  [ P ] - Parado (0,02 €/s)")
    print("  [ F ] - Finalizar carrera")
    print("  [ S ] - Salir del sistema")
    print("-" * 35)

def main():
    taximeter = Taximeter()

    while True:
        print_menu()
        command = input("\nIntroduzca la letra correspondiente a la acción que desee realizar: ").strip().upper()
        
        if command == 'I':
            if taximeter.is_running:
                print("⚠️ Ya existe una carrera en curso")
            else:
                taximeter.start_ride()
                print("🟢 Carrera INICIADA. El taxímetro está funcionando (Estado actual: PARADO)")
                
        elif command == 'M':
            if not taximeter.is_running:
                print("⚠️ Primero debes iniciar una carrera")
            else:
                taximeter.change_state(State.MOVING)
                print(f"⏩ El estado ha cambiado a EN MOVIMIENTO. Importe total actual: {taximeter.calculate_current_total():.2f} €")
                
        elif command == 'P':
            if not taximeter.is_running:
                print("⚠️ Primero debes iniciar una carrera")
            else:
                taximeter.change_state(State.STOPPED)
                print(f"🛑 El estado ha cambiado a PARADO. Importe total actual: {taximeter.calculate_current_total():.2f} €")
                
        elif command == 'F':
            if not taximeter.is_running:
                print("⚠️ No hay ninguna carrera en curso que finalizar")
            else:
                total_to_pay = taximeter.finish_ride()
                print("=" * 35)
                print(f"🏁 CARRERA FINALIZADA")
                print(f"💰 IMPORTE TOTAL A COBRAR: {total_to_pay:.2f} €")
                print("=" * 35)
                print("Listo para la siguiente carrera. Pulse [ I ] para iniciar")
                
        elif command == 'S':
            print("Apagando el sistema...")
            break
            
        else:
            print("❌ Comando desconocido")

if __name__ == "__main__":
    main()