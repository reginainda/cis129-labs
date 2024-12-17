# Starting System SIT system = Self inflating tire system 
starting_SIT syestem 
starting tire_pressure_sensors

# main loop: monitor tire pressure continuously
While driving_car:
    for every tire:
    orignal_pressure = read_tire_pressure

# if pressure is below desired pressure inflate
if original_pressure < desired_pressure:
    call inflate_tire_pressure 
    print('Inflating')
else:
    print('Tire is at desired pressure')

# system will check again after 3 minutes
    Wait(3 minutes)
    # adjust tire pressure
Function inflate_tire_pressure:
    Activate SIT system
    


