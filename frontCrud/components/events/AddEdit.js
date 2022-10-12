import { useRouter } from 'next/router';
import { useState } from 'react';

import DatePicker from 'react-datepicker';
import "react-datepicker/dist/react-datepicker.css"

import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import * as Yup from 'yup';

import { Link } from 'components';
import { eventService, alertService } from 'services';

 export const AddEdit = (props) => {
    const event = props?.event;
    const isAddMode = !event;
    const router = useRouter();
    const [showPassword, setShowPassword] = useState(false);
    const [startDate, setStartDate] = useState(new Date());

    const validationSchema = Yup.object().shape({
        category: Yup.string()
            .required('Category is required'),
        event_start: Yup.string()
            .required('Event Start is required'),    
        event_end: Yup.string()
            .required('Event End is required'),
        local_player: Yup.string()
            .required('Local Player is required'),
        visitor_player: Yup.string()
            .required('Visitor Player is required')    

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
            ? createEvent(data)
            : updateEvent(user.id, data);
    }

    const createEvent = (data) => {
        return eventService.create(data)
            .then(() => {
                alertService.success('Event added', { keepAfterRouteChange: true });
                router.push('.');
            })
            .catch(alertService.error);
    }

    const updateEvent = (id, data) => {
        return eventService.update(id, data)
            .then(() => {
                alertService.success('Event updated', { keepAfterRouteChange: true });
                router.push('..');
            })
            .catch(alertService.error);
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <h1>{isAddMode ? 'Add Event' : 'Edit Event'}</h1>
            <div className="form-row">
                <div className="form-group col-5">
                    <label>Category</label>
                    <input name="category" type="text" {...register('category')} className={`form-control ${errors.nickname ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.category?.message}</div>
                </div>
            </div>
            <div className="form-row">
                <div className="form-group col-5">©√
                    <label>Event Start</label>
                    <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
                </div>
                <div className="form-group col-5">
                    <label>Event End</label>
                    <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
                </div>
            </div>
            <div className="form-row">
                <div className="form-group col-5">
                    <label>Local Player</label>
                    <input name="local_player" type="text" {...register('local_player')} className={`form-control ${errors.nickname ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.local_player?.message}</div>
                </div>
                <div className="form-group col-5">
                    <label>Visitor Player</label>
                    <input name="visitor_player" type="text" {...register('visitor_player')} className={`form-control ${errors.credit ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.visitor_player?.message}</div>
                </div>
            </div>

            <div className="form-row">
                <div className="form-group col-5">
                    <label>Result</label>
                    <input name="result" type="text" {...register('result')} className={`form-control ${errors.nickname ? 'is-invalid' : ''}`} />
                    <div className="invalid-feedback">{errors.result?.message}</div>
                </div>
                <div className="form-group col-5">
                    <label>Goals</label>
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
                    <Link href="/events" className="btn btn-link">Cancel</Link>
                </div>
            </div>
        </form>
    );
}