import { useState, useEffect } from 'react';
import { Link } from '../../components/Link';
import { categoryService } from '../../services/category.service';

const Index = () => {
    const [categorys, setCategorys] = useState(null);

    useEffect(() => {
        categoryService.getAll().then(x => setCategorys(x));
    }, []);

    const deleteCategory = (id) => {
        setCategorys(categorys.map(x => {
            if (x.id === id) { x.isDeleting = true; }
            return x;
        }));
        categoryService.delete(id).then(() => {
            setCategorys(categorys => categorys.filter(x => x.id !== id));
        });
    }

    return (
        <div>
            <h1>Categorys</h1>
            <div style={{position: 'initial', float: 'right'}}>
                <Link href="/eventCategorys/add" className="btn btn-outline-success md-2">+</Link>
            </div>
            
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th style={{ width: '30%' }}>Category Name</th>
                        <th style={{ width: '10%' }}></th>
                    </tr>
                </thead>
                <tbody>
                    {categorys && categorys.map(category =>
                        <tr key={category.id}>
                            <td>{category.name}</td>
                            <td style={{ whiteSpace: 'nowrap' }}>
                                <Link href={`/eventCategorys/edit/${category.id}`} className="btn btn-sm btn-primary mr-1">Edit</Link>
                                <button onClick={() => deleteCategory(category.id)} className="btn btn-sm btn-danger btn-delete-user" disabled={category.isDeleting}>
                                    {category.isDeleting 
                                        ? <span className="spinner-border spinner-border-sm"></span>
                                        : <span>Delete</span>
                                    }
                                </button>
                            </td>
                        </tr>
                    )}
                    {!categorys &&
                        <tr>
                            <td colSpan="4" className="text-center">
                                <div className="spinner-border spinner-border-lg align-center"></div>
                            </td>
                        </tr>
                    }
                    {categorys && !categorys.length &&
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
