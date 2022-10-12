import { playersRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getPlayerRepoById();
        case 'PUT':
            return updatePlayer();
        case 'DELETE':
            return deletePlayer();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getPlayerRepoById() {
        const player = playersRepo.getById(req.query.id);
        return res.status(200).json(player);
    }

    function updatePlayer() {
        try {
            playersRepo.update(req.query.id, req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }

    function deletePlayer() {
        playersRepo.delete(req.query.id);
        return res.status(200).json({});
    }
}
