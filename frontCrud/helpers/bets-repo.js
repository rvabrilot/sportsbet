const fs = require('fs');

let bets = require('data/bets.json');

export const betsRepo = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

function getAll() {
    return bets;
}

function getById(id) {
    return bets.find(x => x.id.toString() === id.toString());
}

function create({ playerName }) {
    const player = {  playerName };
    bet.id = bets.length ? Math.max(...bets.map(x => x.id)) + 1 : 1;
    bets.push(bet);
    saveData();
}

function update(id, { playerName }) {
    const params = { playerName };
    const bet = bets.find(x => x.id.toString() === id.toString());
    Object.assign(bet, params);
    saveData();
}

function _delete(id) {
    bets = bets.filter(x => x.id.toString() !== id.toString());
    saveData();
}

function saveData() {
    fs.writeFileSync('data/bets.json', JSON.stringify(bets, null, 4));
}