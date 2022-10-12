import { AddEdit } from 'components/eventPlayers';
import { playerService } from 'services';

export async function getServerSideProps({ params }) {
    const player = await playerService.getById(params.id);

    return {
        props: { player }
    }
}

export default AddEdit;
