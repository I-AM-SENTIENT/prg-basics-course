def time_string(hours,minutes, time_format):
    if time_format == 12:
        if hours > 12:
            hours -= 12
        return f'{hours}:{minutes:02d} PM'
    else:
        return f'{hours}:{minutes:02d}'
    
    
print(time_string(14, 5, 12))  # Should print 2:05 PM
print(time_string(9, 30, 24))  # Should print 9:30
print(time_string(15, 38, 24)) # Should print 15:38
print(time_string(8, 3, 24))   # Should print 08:03
print(time_string(19, 2, 12))  # Should print 7:02 PM