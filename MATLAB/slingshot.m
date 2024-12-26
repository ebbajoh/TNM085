function slingshot()

    % Constants
    SHIP_MASS = 5;
    G = 5;
    FPS = 60;
    
    % Set starting position and velocity for the spacecraft
    % ÄNDRA STARTPOSITION
    start_position = [-25, -25];
    % ÄNDRA STARTHASTIGHETEN (x-hastighet, y-hastighet)
    start_velocity = [2, 1];
    % Skapa en structure array med allt som behövs för spacecraft
    spacecraft = struct('x', start_position(1), 'y', start_position(2), 'vel_x', start_velocity(1), 'vel_y', start_velocity(2), 'mass', SHIP_MASS);
    
    % Simulation time
    sim_time = 30; % seconds
    dt = 1/FPS;
    num_steps = sim_time * FPS;
    
    % Arrays to store position and velocity data
    positions = zeros(num_steps, 2);
    velocities = zeros(num_steps, 1);
    
    % Simulation loop
    for step = 1:num_steps
        % Store current position and velocity
        positions(step, :) = [spacecraft.x, spacecraft.y];
        velocities(step) = norm([spacecraft.vel_x, spacecraft.vel_y]);
        
        % Move and check collisions for the spacecraft
        spacecraft = move_and_check_collisions(spacecraft, G, dt);
    end
    
    % Plot position in x-y plane
    figure;
    subplot(2, 1, 1);
    plot(positions(:, 1), positions(:, 2));
    hold;
    plot(0,0,'o');
    title('Position of Spacecraft and Planet');
    xlabel('X Position');
    ylabel('Y Position');
    grid on;
    
    % Plot velocity over time
    subplot(2, 1, 2);
    time = linspace(0, sim_time, num_steps);
    plot(time, velocities);
    title('Velocity of Spacecraft over Time');
    xlabel('Time (seconds)');
    ylabel('Velocity (m/s)');
    grid on;

end

function spacecraft = move_and_check_collisions(spacecraft, G, dt)
    % Constants
    PLANET_MASS = 30; %% ÄNDRA DENNA FÖR ATT PÅVERKA VINKELN DEN FÅR EFTER PLANETEN
    
    % Planet position
    planet_position = [0, 0]; %% MARKERAT MED EN RUND CIRCEL
    
    % Calculate distance and force
    distance = sqrt((spacecraft.x - planet_position(1))^2 + (spacecraft.y - planet_position(2))^2);
    force = (G * spacecraft.mass * PLANET_MASS) / distance^2;

    % Calculate acceleration
    acceleration = force / spacecraft.mass;
    angle = atan2(planet_position(2) - spacecraft.y, planet_position(1) - spacecraft.x);

    acceleration_x = acceleration * cos(angle);
    acceleration_y = acceleration * sin(angle);

    % Update velocity
    spacecraft.vel_x = spacecraft.vel_x + acceleration_x * dt;
    spacecraft.vel_y = spacecraft.vel_y + acceleration_y * dt;

    % Update position
    spacecraft.x = spacecraft.x + spacecraft.vel_x * dt;
    spacecraft.y = spacecraft.y + spacecraft.vel_y * dt;
end
