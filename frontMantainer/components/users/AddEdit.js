import { useRouter } from "next/router";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from "yup";

import { Link } from "components";
import { userService, alertService } from "services";

export const AddEdit = (props) => {
  const user = props?.user;
  const isAddMode = !user;
  const router = useRouter();
  const [showPassword, setShowPassword] = useState(false);

  const validationSchema = Yup.object().shape({
    nickname: Yup.string().required("Nick is required"),
    email: Yup.string().email("Email is invalid").required("Email is required"),
    role: Yup.string().required("Role is required"),
    md5: Yup.string()
      .transform((x) => (x === "" ? undefined : x))
      .concat(isAddMode ? Yup.string().required("Password is required") : null)
      .min(6, "Password must be at least 6 characters"),
  });

  const formOptions = { resolver: yupResolver(validationSchema) };

  if (!isAddMode) {
    const { md5, ...defaultValues } = user;
    formOptions.defaultValues = defaultValues;
  }

  const { register, handleSubmit, reset, formState } = useForm(formOptions);
  const { errors } = formState;

  const onSubmit = (data) => {
    return isAddMode ? createUser(data) : updateUser(user.id, data);
  };

  const createUser = (data) => {
    return userService
      .create(data)
      .then(() => {
        alertService.success("User added", { keepAfterRouteChange: true });
        router.push(".");
      })
      .catch(alertService.error);
  };

  const updateUser = (id, data) => {
    return userService
      .update(id, data)
      .then(() => {
        alertService.success("User updated", { keepAfterRouteChange: true });
        router.push("..");
      })
      .catch(alertService.error);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h1>{isAddMode ? "Add User" : "Edit User"}</h1>
      <div className="form-row">
        <div className="form-group col-5">
          <label>Nick Name</label>
          <input
            name="nickname"
            type="text"
            {...register("nickname")}
            className={`form-control ${errors.nickname ? "is-invalid" : ""}`}
          />
          <div className="invalid-feedback">{errors.nickname?.message}</div>
        </div>
      </div>
      <div className="form-row">
        <div className="form-group col-7">
          <label>Email</label>
          <input
            name="email"
            type="text"
            {...register("email")}
            className={`form-control ${errors.email ? "is-invalid" : ""}`}
          />
          <div className="invalid-feedback">{errors.email?.message}</div>
        </div>
        <div className="form-group col">
          <label>Role</label>
          <select
            name="role"
            {...register("role")}
            className={`form-control ${errors.role ? "is-invalid" : ""}`}
          >
            <option value=""></option>
            <option value="User">User</option>
            <option value="Admin">Admin</option>
          </select>
          <div className="invalid-feedback">{errors.role?.message}</div>
        </div>
      </div>
      {!isAddMode && (
        <div>
          <h3 className="pt-3">Change Password</h3>
          <p>Leave blank to keep the same password</p>
        </div>
      )}
      <div className="form-row">
        <div className="form-group col">
          <label>
            Password
            {!isAddMode &&
              (!showPassword ? (
                <span>
                  {" "}
                  -{" "}
                  <a
                    onClick={() => setShowPassword(!showPassword)}
                    className="text-primary"
                  >
                    Show
                  </a>
                </span>
              ) : (
                <em> - {user.md5}</em>
              ))}
          </label>
          <input
            name="md5"
            type="password"
            {...register("md5")}
            className={`form-control ${errors.md5 ? "is-invalid" : ""}`}
          />
          <div className="invalid-feedback">{errors.md5?.message}</div>
        </div>
      </div>
      <div className="form-group">
        <div style={{ position: "initial", float: "right" }}>
          <button
            type="submit"
            disabled={formState.isSubmitting}
            className="btn btn-primary mr-2"
          >
            {formState.isSubmitting && (
              <span className="spinner-border spinner-border-sm mr-1"></span>
            )}
            Save
          </button>
          <button
            onClick={() => reset(formOptions.defaultValues)}
            type="button"
            disabled={formState.isSubmitting}
            className="btn btn-secondary"
          >
            Reset
          </button>
          <Link href="/users" className="btn btn-link">
            Cancel
          </Link>
        </div>
      </div>
    </form>
  );
};
