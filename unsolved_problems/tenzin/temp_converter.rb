def temp_converter

puts "For Celsius to Fahrenheit converter, type CF"
puts 'For Fahrenheit to Celcius converter, type FC'

converter_choice = gets.chomp.downcase



if converter_choice == "cf".chomp
    puts "Type a temperature in celsius please!"
    celcius_temperature = gets.chomp
    number = Float( celcius_temperature ) rescue nil
    if number.nil? 
        puts "#{celcius_temperature} is not a number"
    else
        number * 9/5.0 + 32
    end

elsif converter_choice == 'fc'
    puts "Type a temperature in fahrenheit please!"
    fahrenheit_temperature = gets.chomp
    number = Float( fahrenheit_temperature ) rescue nil
    if number.nil? 
        puts "#{fahrenheit_temperature} is not a number"
    else
       (number - 32) * 5.0/9
    end

else 
    puts "Please pick a valid option! That was neither 'cf' or 'fc'."
    
end


end

puts temp_converter

