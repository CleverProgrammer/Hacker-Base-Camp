def temp_converter

puts "For Celsius to Fahrenheit converter, type CF"
puts 'For Fahrenheit to Celcius converter, type FC'

converter_choice = gets.chomp.downcase



if converter_choice == "cf".chomp
    puts "Type a temperature in celsius please!"
    celcius_temperature = gets.chomp.to_i
    if celcius_temperature.is_a? Integer 
        celcius_temperature * (9/5.0) + 32
    else 
        puts "Please enter a number! That wasn't a number."
    end

elsif converter_choice == 'fc'
    puts "Type a temperature in fahrenheit please!"
    fahrenheit_temperature = gets.chomp.to_i
    if fahrenheit_temperature.is_a? Integer
        (fahrenheit_temperature - 32) * (5/9.0)
    else 
        puts "Please enter a number! That wasn't a number."
    end

else 
    puts "Please pick a valid option! That was neither 'cf' or 'fc'."
    
end


end

temp_converter

