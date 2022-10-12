import { categorysRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getCategorys();
        case 'POST':
            return createCategory();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getCategorys() {
        const categorys = categorysRepo.getAll();
        return res.status(200).json(categorys);
    }
    
    function createCategory() {
        try {
            categorysRepo.create(req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }
}
