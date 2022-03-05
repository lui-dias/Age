from age.entity import Entity, Skill, AttackType

class Warrior(Entity):
    def skill__attack(self):
        return Skill(
            name          = 'attack',
            attack_damage = 50,
            cooldown      = 0,
            magic_power   = 0,
            attack_type   = AttackType.PHYSIC,
            description   = 'A basic attack'
        )

class Mage(Entity):
    def skill__fireball(self):
        return Skill(
            name          = 'fireball',
            attack_damage = 50,
            cooldown      = 0,
            magic_power   = 50,
            attack_type   = AttackType.MAGIC,
            description   = 'A fireball'
        )

class Dummy(Entity):
    ...
