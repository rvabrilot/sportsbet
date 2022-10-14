const fs = require('fs');

let users = require('data/users.json');

export const usersRepo = {
    getAll,
    getById,
    create,
    update,
    delete: _delete
};

function getAll() {
    return users;
}

function getById(id) {
    return users.find(x => x.id.toString() === id.toString());
}

function create({ nickname, email, role, md5 }) {
    const user = { nickname, email, role, md5 };

    console.log('user:::', user);

    // validate
    if (users.find(x => x.id === user.id))
        throw `User with the id ${user.id} already exists`;


    // add and save user
    users.push(user);
    saveData();
}

function update(id, { nickname, credit, email, role, md5 }) {
    const params = { nickname, credit, email, role, md5 };
    const user = users.find(x => x.id.toString() === id.toString());

    // validate
    if (params.email !== user.email && users.find(x => x.email === params.email))
        throw `User with the email ${params.email} already exists`;

    // only update password if entered
    if (!params.md5) {
        delete params.md5;
    }

    // set date updated
    user.dateUpdated = new Date().toISOString();

    // update and save
    Object.assign(user, params);
    saveData();
}

// prefixed with underscore '_' because 'delete' is a reserved word in javascript
function _delete(id) {
    // filter out deleted user and save
    users = users.filter(x => x.id.toString() !== id.toString());
    saveData();
}

// private helper functions
function saveData() {
    fs.writeFileSync('data/users.json', JSON.stringify(users, null, 4));
}