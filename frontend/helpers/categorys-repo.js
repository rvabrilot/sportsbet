const fs = require('fs');

let categorys = require('data/categorys.json');

export const categorysRepo = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

function getAll() {
    return categorys;
}

function getById(id) {
    return categorys.find(x => x.id.toString() === id.toString());
}

function create({ categoryName }) {
    const category = {  categoryName };
    category.id = categorys.length ? Math.max(...categorys.map(x => x.id)) + 1 : 1;
    categorys.push(category);
    saveData();
}

function update(id, { categoryName }) {
    const params = { categoryName };
    const category = categorys.find(x => x.id.toString() === id.toString());
    Object.assign(category, params);
    saveData();
}

function _delete(id) {
    categorys = categorys.filter(x => x.id.toString() !== id.toString());
    saveData();
}

function saveData() {
    fs.writeFileSync('data/categorys.json', JSON.stringify(categorys, null, 4));
}