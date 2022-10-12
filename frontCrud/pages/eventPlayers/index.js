import { useState, useEffect } from 'react';
import { Link } from '../../components/Link';
import { playerService } from '../../services/player.service';

const Index = () => {
    const [players, setPlayers] = useState(null);

    useEffect(() => {
        playerService.getAll().then(x => setPlayers(x));
    }, []);

    const deletePlayer = (id) => {
        playerService(players.map(x => {
            if (x.id === id) { x.isDeleting = true; }
            return x;
        }));
        playerService.delete(id).then(() => {
            setPlayers(players => players.filter(x => x.id !== id));
        });
    }

    return (
        <div>
            <h1>Players</h1>
            <div style={{position: 'initial', float: 'right'}}>
                <Link href="/eventPlayers/add" className="btn btn-outline-success md-2">+</Link>
            </div>
            
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th style={{ width: '30%' }}>Player Name</th>
                        <th style={{ width: '10%' }}></th>
                    </tr>
                </thead>
                <tbody>
                    {players && players.map(player =>
                        <tr key={player.id}>
                            <td>{player.name}</td>
                            <td style={{ whiteSpace: 'nowrap' }}>
                                <Link href={`/eventPlayers/edit/${player.id}`} className="btn btn-sm btn-primary mr-1">Edit</Link>
                                <button onClick={() => deletePlayer(player.id)} className="btn btn-sm btn-danger btn-delete-user" disabled={player.isDeleting}>
                                    {player.isDeleting 
                                        ? <span className="spinner-border spinner-border-sm"></span>
                                        : <span>Delete</span>
                                    }
                                </button>
                            </td>
                        </tr>
                    )}
                    {!players &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="spinner-border spinner-border-lg align-center"></div>
                            </td>
                        </tr>
                    }
                    {players && !players.length &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="p-2">No category To Display</div>
                            </td>
                        </tr>
                    }
                </tbody>
            </table>
        </div>
    );
}

export default Index;
