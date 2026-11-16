import logging
from taximeter import Taximeter, State

logging.basicConfig(
    filename='taximetro.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def print_menu(taximeter):
    print("🚕 TaxiTech - Terminal para conductores")
    print("-" * 35)
    print("  [ I ] - Iniciar carrera")
    print(f"  [ M ] - En movimiento ({taximeter.moving_fare:.2f} €/s)")
    print(f"  [ P ] - Parado ({taximeter.stopped_fare:.2f} €/s)")
    print("  [ F ] - Finalizar carrera")
    print("  [ V ] - Ver histórico de carreras")
    print("  [ S ] - Salir del sistema")
    print("-" * 35)

def main():
    taximeter = Taximeter()

    while True:
        print_menu(taximeter)
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

        elif command == 'V':
            historial = taximeter.get_history()
            print("\n" + "=" * 35)
            print("📊 HISTÓRICO DE CARRERAS")
            if not historial:
                print("No hay carreras registradas")
            else:
                for carrera in historial:
                    print(f"📅 Fecha: {carrera['fecha']} | ⏱️  Duración: {carrera['duracion']:.1f}s | 💰 Importe: {carrera['total']:.2f} €")
            print("=" * 35)
                
        elif command == 'S':
            print("Apagando el sistema...")
            break
            
        else:
            print("❌ Comando desconocido")

if __name__ == "__main__":
    main()