import { AddEdit } from 'components/events';
import { eventService } from 'services';

export async function getServerSideProps({ params }) {
    const event = await eventService.getById(params.id);

    return {
        props: { event }
    }
}

export default AddEdit;
