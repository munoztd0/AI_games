/** Exporté le 1/21/2022, 9:53:47 PM **/

/** noobAI **/

/** functions **/

//--------------------------------
//--------- Fonctions -------------
//--------------------------------

function canMoveAttackWithWeapon(weapon, enemyLeek) {
	// Si on peut déjà lui tirer dessus c'est pas la peine de calculer
	if(canUseWeapon(weapon, enemyLeek)) return getCell();
	var remainingMP = getMP();
	var myCell = getCell();
	var distance = getCellDistance(myCell, getCell(enemyLeek));
	// Si l'ennemi est bien a notre portée théorique
	if(distance <= remainingMP + getWeaponMaxRange(weapon)) {
		var cells = getCellsToUseWeapon(weapon, enemyLeek);
		for(var i = 0; i < count(cells); i++) {
			var pathLength = getPathLength(myCell, cells[i]);
			if(pathLength <= remainingMP) return cells[i];
		}
	}
	return false;
}


global attackChip = [
		CHIP_ROCK,
		CHIP_ROCK,
		CHIP_ICE
];

// Fonction qui retourne la portée maximale des puces/armes d'un poireau
function getMaxRange(leek){
	var maxRange = 0;
	// On boucle sur les armes
	for(var weapon in getWeapons(leek)){
		if(getWeaponMaxRange(weapon) > maxRange) maxRange = getWeaponMaxRange(weapon);
	}
	// On boucle sur les puces
	for(var chip in attackChip){
		if(getChipMaxRange(chip) > maxRange) maxRange = getChipMaxRange(chip);
	}
	return maxRange;
}

// Fonction qui retourne le nombre maximal de PM qu'il faut utiliser pour ne pas se faire toucher au prochain tour
// Retourne 0 si le résulta est négatif
function getMaxMPToSafeMove(enemyLeek){
	var maxRange = getMaxRange(enemyLeek); // Portée maximale
	var maxRangeNextTurn = maxRange + getMP(enemyLeek); // Portée maximale du prochain tour
	var distance = getCellDistance(getCell(), getCell(enemyLeek)); // Distance entre les poireaux
	var maxPMSafe = distance - (maxRangeNextTurn + 1); // +1 car la portée commence à 0
	return max(0,maxPMSafe);
}


function tacticMoveToward(enemy, strat) {
	if(strat == "rush") moveToward(enemy, enemy);
	else moveToward(enemy, getMaxMPToSafeMove(enemy));
}



global phrases = [
    "Tu es cuit [leek] !",
    "Tu vas finir en vinaigrette [leek] !",
    "Les carottes sont cuites [leek] !",
    "je vais te tailler en julienne [leek] !",
    "Je vais t'assaisonner [leek] !"
	"Bachibozook !"
];

function menace(ennemy){
    var phrase = random(phrases);
    return replace(phrase, "[leek]", getName(ennemy));
}

function random(array){
    return array[randInt(0, count(array))];
}


function getRealNearestEnemy(me){
	var nearestEnemy = getNearestEnemy();
	var nbEnemy = getAliveEnemiesCount();
	if(!isSummon(nearestEnemy) or nbEnemy <= 1) return nearestEnemy;
	
	var secondNearestEnemy = getNearestEnemyTo(nearestEnemy);
	if(!isSummon(secondNearestEnemy)) return secondNearestEnemy;
	
	var enemies = getAliveEnemies();
	var realNearestEnemy = nearestEnemy;
	var realNearestEnemyDistance = 1000;
	for(var enemy in enemies) {
		if(enemy != nearestEnemy and enemy != secondNearestEnemy) {
			var enemyDistance = getCellDistance(me, enemy);
			if(enemyDistance < realNearestEnemyDistance) {
				realNearestEnemy = enemy;
				realNearestEnemyDistance = enemyDistance;
			}
		}
	}
	return realNearestEnemy;
}

function useComboOnMe(combo, me){
	for(var comboItem in combo) {
		attackWithChip(comboItem["id"], me);
	}
}

function attack(weapon, enemy) {
		useWeapon(enemy);
		useWeapon(enemy);
}
function attackWithChip(chip, enemy) {
		useChip(chip, enemy);
		useChip(chip, enemy);
		useChip(chip, enemy);
}

// Renvoi une cellule atteignable où l'on peut pucer un ennemi, sinon renvoi false
function canMoveAttackWithChip(chip, enemyLeek) {
	// Si on peut déjà le pucer dessus c'est pas la peine de calculer
	if(canUseChip(chip, enemyLeek)) return getCell();
	var remainingMP = getMP();
	var myCell = getCell();
	var distance = getCellDistance(myCell, getCell(enemyLeek));
	// Si l'ennemi est bien a notre portée théorique
	if(distance <= remainingMP + getChipMaxRange(chip)) {
		var cells = getCellsToUseChip(chip, enemyLeek);
		for(var i = 0; i < count(cells); i++) {
			var pathLength = getPathLength(myCell, cells[i]);
			if(pathLength <= remainingMP) return cells[i];
		}
	}
	return false;
}

function useAttackCombo(combo, enemy, strat){
	for(var comboItem in combo) {
		if(comboItem["type"] == "puce") {
			var cellToPuce = canMoveAttackWithChip(comboItem["id"], enemy);
			if(cellToPuce != false) {
				moveTowardCell(cellToPuce);
				attackWithChip(comboItem["id"], enemy);
				if(strat == "rush") moveToward(enemy);
				else moveAwayFrom(enemy);
			}
		}
		if(comboItem["type"] == "weapon") {
			var cellToWeapon = canMoveAttackWithWeapon(comboItem["id"], enemy);
			//debug(cellToWeapon);
			if(cellToWeapon != false) {
				moveTowardCell(cellToWeapon);
				attack(comboItem["id"], enemy);
				moveAwayFrom(enemy);
			}
		}
	}
}

function UseProtectionFirstTime(enemyLeek){
    var val = false;
    //debug(getMaxMPToSafeMove(enemyLeek));
    //debug(getMaxRange(enemyLeek));
    if ( (getMaxMPToSafeMove(enemyLeek) > 0) && ( getMaxMPToSafeMove(enemyLeek) < 6 ) ) {
    //if ( getMaxMPToSafeMove(enemyLeek) <= 6 ) {
        val = true;
    }
    return val;
}




// --- Variables ---
var weapon = getWeapon();
var me = getEntity();
var enemy = getRealNearestEnemy(me);
var turn = getTurn();
var heal = CHIP_CURE
var chip = CHIP_ROCK

global attackCombo;
if(attackCombo == null) {
	attackCombo = [];

	attackCombo[0] = [];
	attackCombo[0]["type"] = "puce";
	attackCombo[0]["id"] = CHIP_ROCK;

	attackCombo[1] = [];
	attackCombo[1]["type"] = "weapon";
	attackCombo[1]["id"] = WEAPON_MAGNUM;

	attackCombo[2] = [];
	attackCombo[2]["type"] = "puce";
	attackCombo[2]["id"] = CHIP_ICE;

	//attackCombo[3] = [];
	//attackCombo[3]["type"] = "puce";
	//attackCombo[3]["id"] = CHIP_ICE;
}

global buffCombo;
if(buffCombo == null) {
	buffCombo = [];

	buffCombo[0] = [];
	buffCombo[0]["type"] = "puce";
	buffCombo[0]["id"] = CHIP_HELMET;

	buffCombo[0] = [];
	buffCombo[0]["type"] = "puce";
	buffCombo[0]["id"] = CHIP_WALL;
}

global healCombo;
if(healCombo == null) {
	healCombo = [];

	healCombo[0] = [];
	healCombo[0]["type"] = "puce";
	healCombo[0]["id"] = CHIP_BANDAGE;
}

global tactic;
if(tactic == null) {
	tactic = "hit&run";
}


if(isAlive(enemy) == true) {
	
	// --- Code ---

	// On prend l'arme
	if(weapon == null) {
		setWeapon(WEAPON_MAGNUM);
		weapon = WEAPON_MAGNUM;
	}



	if(turn > 50) tactic = "rush";

	if(UseProtectionFirstTime(enemy) && getLife(enemy) > 100) {
		// On utilise le combo de buff
		useComboOnMe(buffCombo, me);
	}

	say(menace(enemy));

	if(turn % 4 == 0){
		useChip(CHIP_PROTEIN, me);
	}

	//if((turn + 2) % 4 == 0){
		//useChip(CHIP_PROTEIN, me);
	//}


	// On utilise le combo d'attaque
	if(isAlive(enemy) == true) {
		useAttackCombo(attackCombo, enemy, tactic); 
	}
	// On se rapproche en restant en zone safe
	tacticMoveToward(enemy, tactic);

	if(turn > 2) {
		// On utilise le combo de buff
		useComboOnMe(buffCombo, me);
	}


	if( getLife() < getTotalLife()/2 ) 
		useChip(heal, me);
}
