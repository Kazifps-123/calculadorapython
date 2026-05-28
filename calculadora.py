import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        resultado = ""
        etapas = ""

        if operacao == "sqrt":
            if num1 < 0:
                resultado = "Erro"
                etapas = "Não existe raiz real de número negativo."
            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"

        elif operacao == "log":
            if num1 <= 0:
                resultado = "Erro"
                etapas = "Logaritmo só existe para números positivos."
            else:
                resultado = math.log10(num1)
                etapas = f"log({num1}) = {resultado}"

        elif operacao == "bhaskara":
            num2 = float(request.form["num2"])
            num3 = float(request.form["num3"])

            a = num1
            b = num2
            c = num3

            delta = b**2 - 4*a*c

            if delta < 0:
                resultado = "Erro"
                etapas = "Delta negativo. Não existem raízes reais."
            else:
                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)

                resultado = f"x1 = {x1} | x2 = {x2}"
                etapas = f"Δ = {delta}"

        else:
            num2 = float(request.form["num2"])

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2}"

            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2}"

            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} × {num2}"

            elif operacao == "/":
                if num2 == 0:
                    resultado = "Erro"
                    etapas = "Não é possível dividir por zero."
                else:
                    resultado = num1 / num2
                    etapas = f"{num1} ÷ {num2}"

            elif operacao == "**":
                resultado = num1 ** num2
                etapas = f"{num1}^{num2}"

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado
        )

    except:
        return render_template(
            "calculadora.html",
            etapas="Erro ao calcular.",
            resultados=""
        )
