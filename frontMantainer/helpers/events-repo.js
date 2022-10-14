const fs = require('fs');

let events = require('data/events.json');

export const eventsRepo = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};
   
function getAll() {
    return events;
}

function getById(id) {
    return events.find(x => x.id.toString() === id.toString());
}

function create({ name }) {
    const category = {  name };
    category.id = categorys.length ? Math.max(...categorys.map(x => x.id)) + 1 : 1;
    categorys.push(category);
    saveData();
}

function update(id, { name }) {
    const params = { name };
    const category = categorys.find(x => x.id.toString() === id.toString());
    Object.assign(category, params);
    saveData();
}

function _delete(id) {
    categorys = categorys.filter(x => x.id.toString() !== id.toString());
    saveData();
}

function saveData() {
    fs.writeFileSync('data/events.json', JSON.stringify(categorys, null, 4));
}