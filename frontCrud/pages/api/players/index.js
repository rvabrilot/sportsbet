import { playersRepo } from 'helpers';

export default handler;

function handler(req, res) {
    switch (req.method) {
        case 'GET':
            return getPlayers();
        case 'POST':
            return createPlayer();
        default:
            return res.status(405).end(`Method ${req.method} Not Allowed`)
    }

    function getPlayers() {
        const players = playersRepo.getAll();
        return res.status(200).json(players);
    }
    
    function createPlayer() {
        try {
            playersRepo.create(req.body);
            return res.status(200).json({});
        } catch (error) {
            return res.status(400).json({ message: error });
        }
    }
}
