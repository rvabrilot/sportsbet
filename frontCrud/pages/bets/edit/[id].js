import { AddEdit } from 'components/bets';
import { betService } from 'services';

export async function getServerSideProps({ params }) {
    const bet = await playerService.getById(params.id);

    return {
        props: { bet }
    }
}

export default AddEdit;
