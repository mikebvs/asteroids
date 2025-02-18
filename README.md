# Asteroids
### This project was made to practice multi-file projects and inheritance within Python. Using Pygame we were able to create a living game that acted out the classic Asteroids along with some Additional Content outside the game's original scope.

## Additional Content
### Spiral Shot
1. This is an ability used by the player that fires a number of projectiles in sequence radially over a duration radially around the player
2. This ability has a 10s Cooldown
3. Cooldown, Projectile Modifier, and Duration are modifiable in the constants.md file
### Radial Shot
1. This ability fires a modifiable number of projectiles simultaneously around the playter character
2. The projectiles are evenly distributed in a 360 degree radius around the player
3. This ability has a 10s Cooldown
4. The Cooldown is modifiable in the constants.md file
### Player Collision Cooldown
1. This prevents the player from triggering collision detection more than once every 2 seconds
2. During the collision cooldown the player will flash red to indicate they cannot be damaged during the duration.
3. This duration is modifiable in the constants.md file
### Player Lives
1. The player has 5 lives
2. This value is modifiable within the constants.md file