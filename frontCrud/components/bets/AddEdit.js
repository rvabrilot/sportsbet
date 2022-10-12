import { useRouter } from 'next/router';
import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';

import { Link } from 'components';
import { userService, alertService } from 'services';

 export const AddEdit = (props) => {
    const user = props?.user;
    const isAddMode = !user;
    const router = useRouter();
    const [showPassword, setShowPassword] = useState(false);
    
    const validationSchema = Yup.object().shape({
        nickname: Yup.string()
            .required('Nick is required'),
        credit: Yup.string()
            .required('Credit is required'),    
        email: Yup.string()
            .email('Email is invalid')
            .required('Email is required'),
        role: Yup.string()
            .required('Role is required'),
         md5: Yup.string()
            .transform(x => x === '' ? undefined : x)
            .concat(isAddMode ? Yup.string().required('Password is required') : null)
            .min(6, 'Password must be at least 6 characters'),
        confirmPassword: Yup.string()
            .transform(x => x === '' ? undefined : x)
            .when('md5', (md5, schema) => {
                if (md5 || isAddMode) return schema.required('Confirm Password is required');
            })
            .oneOf([Yup.ref('md5')], 'Passwords must match')
    });
    const formOptions = { resolver: yupResolver(validationSchema) };

    if (!isAddMode) {
        const { md5, confirmPassword, ...defaultValues } = user;
        formOptions.defaultValues = defaultValues;
    }

    const { register, handleSubmit, reset, formState } = useForm(formOptions);
    const { errors } = formState;

    const onSubmit = (data) => {
        return isAddMode
            ? createUser(data)
            : updateUser(user.id, data);
    }

    const createUser = (data) => {
        return userService.create(data)
            .then(() => {
                alertService.success('User added', { keepAfterRouteChange: true });
                router.push('.');
            })
            .catch(alertService.error);
    }

    const updateUser = (id, data) => {
        return userService.update(id, data)
            .then(() => {
                alertService.success('User updated', { keepAfterRouteChange: true });
                router.push('..');
            })
            .catch(alertService.error);
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <h1>{isAddMode ? 'Add Bet' : 'Edit Bet'}</h1>
            <div className="form-row">
                <div className="form-group col-5">
                    <label>Player</label>
                    <input name="result" type="text" {...register('result')} className={`form-control ${errors.nickname ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.result?.message}</div>
                </div>

                <div className="form-group col-5">
                    <label>Player Date</label>
                    <input name="goals" type="text" {...register('goals')} className={`form-control ${errors.credit ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.goals?.message}</div>
                </div>
            </div>
            <div className="form-row">
                <div className="form-group col-5">
                    <label>Result</label>
                    <input name="result" type="text" {...register('result')} className={`form-control ${errors.nickname ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.result?.message}</div>
                </div>

                <div className="form-group col-5">
                    <label>goals</label>
                    <input name="goals" type="text" {...register('goals')} className={`form-control ${errors.credit ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.goals?.message}</div>
                </div>
            </div>

            <div className="form-group"> 
            <div style={{position: 'initial', float: 'right'}}>
                <button type="submit" disabled={formState.isSubmitting} className="btn btn-primary mr-2">
                    {formState.isSubmitting && <span className="spinner-border spinner-border-sm mr-1"></span>}
                    Save
                </button>
                <button onClick={() => reset(formOptions.defaultValues)} type="button" disabled={formState.isSubmitting} className="btn btn-secondary">Reset</button>
                <Link href="/bets" className="btn btn-link">Cancel</Link>
                </div>
                </div>
        </form>
    );
}