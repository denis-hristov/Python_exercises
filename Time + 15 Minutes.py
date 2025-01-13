hours = int(input())
minutes = int(input())

hours_to_minutes = hours*60
sum = hours_to_minutes+minutes+15

end_hours = sum//60
end_minutes = sum%60

if end_hours>23:
    end_hours = 0

print(f"{end_hours}:{end_minutes:02d}")

