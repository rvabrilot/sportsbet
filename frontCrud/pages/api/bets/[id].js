import { categorysRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getCategoryRepoById();
        case 'PUT':
            return updateCategory();
        case 'DELETE':
            return deleteCategory();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getCategoryRepoById() {
        const category = categorysRepo.getById(req.query.id);
        return res.status(200).json(category);
    }

    function updateCategory() {
        try {
            categorysRepo.update(req.query.id, req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }

    function deleteCategory() {
        categorysRepo.delete(req.query.id);
        return res.status(200).json({});
    }
}
