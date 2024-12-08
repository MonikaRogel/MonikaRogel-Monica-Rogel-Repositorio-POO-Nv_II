# Semana 03 Monica Rogel Tema(POO)

# Clase que representa el clima de un día
class WeatherDay:
    def __init__(self, temperature=0.0, humidity=0.0):
        """
        Inicializa un objeto de tipo WeatherDay con la temperatura y la humedad.

        Parámetros:
        temperature (float): Temperatura del día en grados Celsius.
        humidity (float): Porcentaje de humedad del día.
        """
        self.__temperature = temperature  # Atributo privado para almacenar la temperatura
        self.__humidity = humidity  # Atributo privado para almacenar la humedad

    def set_temperature(self, temperature):
        """
        Establece la temperatura del día, asegurándose de que esté dentro de un rango válido.

        Parámetros:
        temperature (float): Temperatura en grados Celsius.

        Excepciones:
        ValueError: Si la temperatura no está en el rango de -50°C a 60°C.
        """
        if -50 <= temperature <= 60:
            self.__temperature = temperature
        else:
            raise ValueError("La temperatura debe estar entre -50 y 60°C.")

    def get_temperature(self):
        """
        Obtiene la temperatura del día.

        Retorna:
        float: Temperatura en grados Celsius.
        """
        return self.__temperature

    def set_humidity(self, humidity):
        """
        Establece el porcentaje de humedad del día, asegurándose de que esté dentro de un rango válido.

        Parámetros:
        humidity (float): Porcentaje de humedad.

        Excepciones:
        ValueError: Si la humedad no está en el rango de 0% a 100%.
        """
        if 0 <= humidity <= 100:
            self.__humidity = humidity
        else:
            raise ValueError("La humedad debe estar entre 0% y 100%.")

    def get_humidity(self):
        """
        Obtiene el porcentaje de humedad del día.

        Retorna:
        float: Porcentaje de humedad.
        """
        return self.__humidity

    def display(self):
        """
        Muestra de manera legible la información del día, incluyendo la temperatura y la humedad.
        """
        print(f"Temperatura: {self.__temperature}°C, Humedad: {self.__humidity}%")


# Clase que representa toda una semana de datos del clima
class WeatherWeek:
    def __init__(self):
        """
        Inicializa un objeto de tipo WeatherWeek para almacenar los datos de la semana.

        Atributos:
        __days (list): Lista que almacena los objetos de tipo WeatherDay.
        """
        self.__days = []

    def add_day(self, weather_day):
        """
        Agrega un objeto de tipo WeatherDay a la semana.

        Parámetros:
        weather_day (WeatherDay): Un objeto que representa un día de clima.

        Excepciones:
        ValueError: Si ya se han agregado 7 días.
        TypeError: Si el objeto no es de tipo WeatherDay.
        """
        if isinstance(weather_day, WeatherDay):
            if len(self.__days) < 7:
                self.__days.append(weather_day)
            else:
                raise ValueError("Solo puedes agregar hasta 7 días.")
        else:
            raise TypeError("Solo se pueden agregar objetos de tipo WeatherDay.")

    def calculate_average_temperature(self):
        """
        Calcula el promedio de la temperatura de todos los días de la semana.

        Retorna:
        float: Promedio de las temperaturas.

        Excepciones:
        ValueError: Si no se han agregado días para calcular el promedio.
        """
        if len(self.__days) == 0:
            raise ValueError("No se han agregado días para calcular el promedio.")
        total_temp = sum(day.get_temperature() for day in self.__days)
        return total_temp / len(self.__days)

    def display_week(self):
        """
        Muestra la información de todos los días de la semana, incluyendo temperatura y humedad.
        """
        print("Datos del clima de la semana:")
        for i, day in enumerate(self.__days, start=1):
            print(f"Día {i}: ", end="")
            day.display()


# Clase hija que extiende la funcionalidad de WeatherDay para agregar una condición climática
class ExtendedWeatherDay(WeatherDay):
    def __init__(self, temperature=0.0, humidity=0.0, condition="Despejado"):
        """
        Inicializa un objeto de tipo ExtendedWeatherDay, agregando la condición climática.

        Parámetros:
        temperature (float): Temperatura en grados Celsius.
        humidity (float): Porcentaje de humedad.
        condition (str): Condición climática del día (Despejado, Lluvioso, Nublado).
        """
        super().__init__(temperature, humidity)  # Llamada al constructor de la clase base
        self.__condition = condition  # Atributo privado para almacenar la condición climática

    def set_condition(self, condition):
        """
        Establece la condición climática del día, asegurándose de que esté dentro de un conjunto válido.

        Parámetros:
        condition (str): Condición climática (Despejado, Lluvioso, Nublado).

        Excepciones:
        ValueError: Si la condición no es válida.
        """
        valid_conditions = ["Despejado", "Lluvioso", "Nublado"]
        if condition not in valid_conditions:
            raise ValueError("Condición no válida. Debe ser una de las siguientes: Despejado, Lluvioso, Nublado.")
        self.__condition = condition

    def get_condition(self):
        """
        Obtiene la condición climática del día.

        Retorna:
        str: Condición climática (Despejado, Lluvioso, Nublado).
        """
        return self.__condition

    def display(self):
        """
        Muestra de manera legible la información del día, incluyendo la temperatura, humedad y condición climática.
        """
        print(
            f"Temperatura: {self.get_temperature()}°C, Humedad: {self.get_humidity()}%, Condición: {self.__condition}"
        )


# Aquí empieza el flujo principal del programa
def main():
    """
    Función principal que gestiona la entrada de datos del clima para una semana,
    calcula el promedio de la temperatura y muestra un resumen de la semana.
    """
    week = WeatherWeek()  # Creamos una instancia de WeatherWeek para manejar toda la semana

    print("Ingresa los datos del clima para la semana:")
    for i in range(7):
        print(f"\nDía {i + 1}:")
        try:
            # Pedimos al usuario los datos del clima
            temp = float(input("Ingresa la temperatura (°C): "))
            hum = float(input("Ingresa la humedad (%): "))
            condition = input("Ingresa la condición (Despejado, Lluvioso, Nublado): ")

            # Creamos un objeto del día con los datos ingresados
            day = ExtendedWeatherDay(temp, hum, condition)
            week.add_day(day)  # Agregamos el día a la semana
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")
            return

    # Mostramos todos los datos de la semana
    print("\nResumen del clima de la semana:")
    week.display_week()

    # Calculamos y mostramos el promedio de la temperatura semanal
    try:
        avg_temp = week.calculate_average_temperature()
        print(f"\nTemperatura promedio semanal: {avg_temp:.2f}°C")
    except ValueError as e:
        print(f"Error: {e}")


# Esta parte asegura que el programa solo se ejecute si lo corremos directamente
if __name__ == "__main__":
    main()


