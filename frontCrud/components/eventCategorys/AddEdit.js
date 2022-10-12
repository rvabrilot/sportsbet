import { useRouter } from 'next/router';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';

import { Link } from 'components';
import { categoryService, alertService } from 'services';

 export const AddEdit = (props) => {
    const category = props?.category;
    const isAddMode = !category;
    const router = useRouter();
    
    const validationSchema = Yup.object().shape({
        name: Yup.string()
        .required('name is required')
    });
    const formOptions = { resolver: yupResolver(validationSchema) };

    if (!isAddMode) {
        const { password, confirmPassword, ...defaultValues } = category;
        formOptions.defaultValues = defaultValues;
    }

    const { register, handleSubmit, reset, formState } = useForm(formOptions);
    const { errors } = formState;

    const onSubmit = (data) => {
        return isAddMode
            ? createCategory(data)
            : updateCategory(category.id, data);
    }

    const createCategory = (data) => {
        return categoryService.create(data)
            .then(() => {
                alertService.success('category added', { keepAfterRouteChange: true });
                router.push('.');
            })
            .catch(alertService.error);
    }

    const updateCategory = (id, data) => {
        return categoryService.update(id, data)
            .then(() => {
                alertService.success('category updated', { keepAfterRouteChange: true });
                router.push('..');
            })
            .catch(alertService.error);
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <h1>{isAddMode ? 'Add category' : 'Edit category'}</h1>
            <div className="form-row">
                <div className="form-group col-5">
                    <label>Category Name</label>
                    <input name="name" type="text" {...register('name')} className={`form-control ${errors.name ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.name?.message}</div>
                </div>
            </div>

            <div className="form-group"> 
            <div style={{position: 'initial', float: 'right'}}>
                <button type="submit" disabled={formState.isSubmitting} className="btn btn-primary mr-2">
                    {formState.isSubmitting && <span className="spinner-border spinner-border-sm mr-1"></span>}
                    Save
                </button>
                <button onClick={() => reset(formOptions.defaultValues)} type="button" disabled={formState.isSubmitting} className="btn btn-secondary">Reset</button>
                <Link href="/eventCategorys" className="btn btn-link">Cancel</Link>
                </div>
                </div>
        </form>
    );
}