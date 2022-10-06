import { AddEdit } from 'components/eventCategorys';
import { categoryService } from 'services';

export async function getServerSideProps({ params }) {
    const category = await categoryService.getById(params.id);

    return {
        props: { category }
    }
}

export default AddEdit;
