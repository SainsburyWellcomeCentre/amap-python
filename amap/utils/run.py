import logging

from pathlib import Path


class Run:
    """
    Determines what parts of amap to run, based on what files already exist
    """

    def __init__(
        self, paths, boundaries=True, additional_images=False, debug=False
    ):
        self.paths = paths
        self._boundaries = boundaries
        self._additional_images = additional_images
        self._debug = debug

    # TODO: make this more specific
    @property
    def preprocess(self):
        if (
            self._registered_atlas_exists
            and self._registered_hemispheres_exists
            and self._inverse_control_point_exists
        ):
            return False
        else:
            return True

    @property
    def register(self):
        if (
            self._registered_atlas_exists
            and self._registered_hemispheres_exists
            and self._inverse_control_point_exists
        ):
            logging.info("Registration allready completed, skipping")
            return False
        else:
            return True

    @property
    def affine(self):
        if self.register and not(
            self._affine_reg_brain_exists or self._control_point_exists
        ):
            return True
        else:
            logging.info("Affine registration allready completed, skipping")
            return False

    @property
    def freeform(self):
        if self.register and not self._control_point_exists:
            return True
        else:
            logging.info("Freeform registration already completed, skipping.")
            return False

    @property
    def segment(self):
        if self._registered_atlas_exists:
            logging.info("Registered atlas exists, skipping segmentation")
            return False
        else:
            return True

    @property
    def hemispheres(self):
        if self._registered_hemispheres_exists:
            logging.info("Registered hemispheres exist, skipping segmentation")
            return False
        else:
            return True

    @property
    def inverse_transform(self):
        if self._inverse_control_point_exists:
            logging.info(
                "Inverse transform exists, skipping inverse registration"
            )
            return False
        else:
            return True

    @property
    def volumes(self):
        if self._volumes_exist:
            logging.info(
                "Volumes csv exists, skipping region volume calculation"
            )
            return False
        else:
            return True

    @property
    def boundaries(self):
        if self._boundaries:
            if self._boundaries_exist:
                logging.info(
                    "Boundary image exists, skipping boundary image generation"
                )
                return False
            else:
                return True
        else:
            logging.info("Boundary image deselected, not generating")
            return False

    @property
    def delete_temp(self):
        return self._debug

    @property
    def _downsampled_exists(self):
        return self._exists(self.paths.downsampled_brain_path)

    @property
    def _downsampled_filtered_exists(self):
        return self._exists(self.paths.tmp__downsampled_filtered)

    @property
    def _affine_exists(self):
        return self._exists(self.paths.affine_matrix_path)

    @property
    def _affine_reg_brain_exists(self):
        return self._exists(self.paths.tmp__affine_registered_atlas_brain_path)

    @property
    def _control_point_exists(self):
        return self._exists(self.paths.control_point_file_path)

    @property
    def _inverse_control_point_exists(self):
        return self._exists(self.paths.inverse_control_point_file_path)

    @property
    def _registered_atlas_exists(self):
        return self._exists(self.paths.registered_atlas_path)

    @property
    def _registered_hemispheres_exists(self):
        return self._exists(self.paths.registered_hemispheres_img_path)

    @property
    def _volumes_exist(self):
        return self._exists(self.paths.volume_csv_path)

    @property
    def _boundaries_exist(self):
        return self._exists(self.paths.boundaries_file_path)

    @staticmethod
    def _exists(path):
        if isinstance(path, Path):
            return path.exists()
        else:
            return Path(path).exists()
