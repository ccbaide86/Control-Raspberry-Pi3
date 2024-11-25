#!/bin/bash

# Configurar los pines como PWM
gpio -g mode 17 pwm
gpio -g mode 22 pwm
gpio -g mode 27 pwm

# Configurar el rango del PWM (puedes ajustarlo según tu hardware)
gpio pwmr 100

# Disminuir brillo (fade out)
for i in {100..0}
do
  gpio -g pwm 17 $i
  gpio -g pwm 22 $i
  gpio -g pwm 27 $i
  sleep 0.25  # Ajusta el tiempo para suavizar el fade
done
