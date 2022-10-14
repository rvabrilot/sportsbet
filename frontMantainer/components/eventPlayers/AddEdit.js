import { useRouter } from "next/router";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import * as Yup from "yup";
import { Link } from "components";
import { playerService, alertService } from "services";

export const AddEdit = (props) => {
  const player = props?.player;
  const isAddMode = !player;
  const router = useRouter();

  const validationSchema = Yup.object().shape({
    name: Yup.string().required("name is required"),
  });
  const formOptions = { resolver: yupResolver(validationSchema) };

  if (!isAddMode) {
    const { password, confirmPassword, ...defaultValues } = player;
    formOptions.defaultValues = defaultValues;
  }

  const { register, handleSubmit, reset, formState } = useForm(formOptions);
  const { errors } = formState;

  const onSubmit = (data) => {
    return isAddMode ? createPlayer(data) : updatePlayer(player.id, data);
  };

  const createPlayer = (data) => {
    return playerService
      .create(data)
      .then(() => {
        alertService.success("category added", { keepAfterRouteChange: true });
        router.push(".");
      })
      .catch(alertService.error);
  };

  const updatePlayer = (id, data) => {
    return playerService
      .update(id, data)
      .then(() => {
        alertService.success("player updated", { keepAfterRouteChange: true });
        router.push("..");
      })
      .catch(alertService.error);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <h1>{isAddMode ? "Add player" : "Edit player"}</h1>
      <div className="form-row">
        <div className="form-group col-5">
          <label>Player Name</label>
          <input
            name="name"
            type="text"
            {...register("name")}
            className={`form-control ${errors.playerName ? "is-invalid" : ""}`}
          />
          <div className="invalid-feedback">{errors.name?.message}</div>
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
          <Link href="/eventPlayers" className="btn btn-link">
            Cancel
          </Link>
        </div>
      </div>
    </form>
  );
};
