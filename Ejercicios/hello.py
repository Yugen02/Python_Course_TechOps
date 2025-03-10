# Esta Variable es un entero
numero = 10
# Esta Variable es un flotante
precio_unitario = 1.99
# multiplicar el numero por el precio unitario
ganacia = numero * precio_unitario
# muestra el resultado
print(ganacia)


print(round(10.939,2))



total = 100
sales_tax_rate = 0.065
taxable = True
if taxable == True:
    print(f"Subtotal : ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = total + sales_tax
print(f"Total : ${total:.2f}")




if condition:
    do indented lines here
    ...
else:
    do indented lines here
    ...
do remaining un-indented lines no matter what.

if condition:
    do these indented lines of code
    ...
elif condition
    do these indented lines of code
    ...
do these un-indented lines of code no matter what