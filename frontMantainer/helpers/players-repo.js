const fs = require("fs");

let players = require("data/players.json");

export const playersRepo = {
  getAll,
  getById,
  create,
  update,
  delete: _delete,
};

function getAll() {
  return players;
}

function getById(id) {
  return players.find((x) => x.id.toString() === id.toString());
}

function create({ name }) {
  const player = { name };
  player.id = players.length ? Math.max(...players.map((x) => x.id)) + 1 : 1;
  players.push(player);
  saveData();
}

function update(id, { name }) {
  const params = { name };
  const player = players.find((x) => x.id.toString() === id.toString());
  Object.assign(player, params);
  saveData();
}

function _delete(id) {
  players = players.filter((x) => x.id.toString() !== id.toString());
  saveData();
}

function saveData() {
  fs.writeFileSync("data/players.json", JSON.stringify(players, null, 4));
}
