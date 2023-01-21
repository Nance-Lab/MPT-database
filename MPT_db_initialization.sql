CREATE TABLE "Biological Sample Info" (
  "Sample_ID" Integer,
  "Sample_type" Varchar,
  "brain_region" Varchar,
  "age_in_days" Integer,
  "gel_density" Varchar,
  PRIMARY KEY ("Sample_ID")
);

CREATE TABLE "ImageJ Parameters" (
  "unique_tif_id" Varchar UNIQUE,
  "Field" Varchar,
  "formulation_id" Varchar,
  "detector" Varchar,
  "tracker" Varchar,
  "video_quality" Varchar,
  "track_duration" Integer,
  "blob_diameter" Integer,
  "linking_max_distance" Integer,
  "gap_closing_max_distnce" Integer,
  "gap_closing_max_fram_gap" Integer,
  PRIMARY KEY ("unique_tif_id"),
  CONSTRAINT "FK_ImageJ Parameters.track_duration"
    FOREIGN KEY ("track_duration")
      REFERENCES "Biological Sample Info"("Sample_ID"),
  CONSTRAINT "tif_id_unique" UNIQUE (unique_tif_id)	
);

CREATE INDEX "Key" ON  "ImageJ Parameters" ("Field");

CREATE TABLE "MPT Raw Data" (
  "timestep_id" Integer,
  "particle_id" Integer UNIQUE,
  "file_name" Varchar UNIQUE,
  "Frame" Integer,
  "Track_ID" Integer,
  "X" Varchar,
  "Y" Varchar,
  "MSDs" Varchar,
  "Gauss" Varchar,
  "Quality" Varchar,
  "SN_ratio" Varchar,
  "Mean_Intensity" Varchar,
  PRIMARY KEY ("timestep_id"),
  CONSTRAINT "FK_MPT Raw Data.file_name"
    FOREIGN KEY ("file_name")
      REFERENCES "ImageJ Parameters"("unique_tif_id")
);

CREATE TABLE "MPT Statistical Features" (
  "particle_id" Integer UNIQUE,
  "file_name" Varchar UNIQUE,
  "Track_ID" Integer,
  "alpha" Varchar,
  "D_fit" Varchar,
  "kurtosis" Varchar,
  "asymmetry1" Varchar,
  "asymmetry2" Varchar,
  "asymmetry3" Varchar,
  "AR" Varchar,
  "elongation" Varchar,
  "boundedness" Varchar,
  "fractal_dim" Varchar,
  "trappedness" Varchar,
  "efficiency" Varchar,
  "straightness" Varchar,
  "MSD_ratio" Varchar,
  "Frames" Varchar,
  "X" Varchar,
  "Y" Varchar,
  "Quality" Varchar,
  "Mean_Intensity" Varchar,
  "SN_ratio" Varchar,
  "Deff1" Varchar,
  "Deff2" Varchar,
  "Mean Alpha" Varchar,
  "Std alpha" Varchar,
  "Mean D_fit" Varchar,
  "Std D_fit" Varchar,
  "Mean kurtosis" Varchar,
  "Mean asymmetry1" Varchar,
  "Std asymmetry1" Varchar,
  "Mean asymmetry2" Varchar,
  "Std asymmetry2" Varchar,
  "Mean asymmetry3" Varchar,
  "Std asymmetry3" Varchar,
  "Mean AR" Varchar,
  "Std AR" Varchar,
  "Mean elongation" Varchar,
  "Std elongation" Varchar,
  "Mean boundedness" Varchar,
  "Std boundedness" Varchar,
  "Mean fractal_dim" Varchar,
  "Std fractal_dim" Varchar,
  "Mean trappedness" Varchar,
  "Mean efficiency" Varchar,
  "Std efficiency" Varchar,
  "Mean straightness" Varchar,
  "Std straightness" Varchar,
  "Mean MSD_ratio" Varchar,
  "Std MSD_ratio" Varchar,
  "Mean frames" Varchar,
  "Std frames" Varchar,
  "Mean X" Varchar,
  "Std X" Varchar,
  "Mean Y" Varchar,
  "Std Y" Varchar,
  "Mean Quality" Varchar,
  "Std Quality" Varchar,
  "Mean Mean_Intensity" Varchar,
  "Std Mean_Intensity" Varchar,
  "Mean SN_Ratio" Varchar,
  "Std SN_Ratio" Varchar,
  "Mean Deff1" Varchar,
  "Std Deff1" Varchar,
  "Mean Deff2" Varchar,
  "Std Deff2" Varchar,
  PRIMARY KEY ("particle_id"),
  CONSTRAINT "FK_MPT Statistical Features.file_name"
    FOREIGN KEY ("file_name")
      REFERENCES "ImageJ Parameters"("unique_tif_id"),
  CONSTRAINT "FK_MPT Statistical Features.particle_id"
    FOREIGN KEY ("particle_id")
      REFERENCES "MPT Raw Data"("particle_id"),
  CONSTRAINT "particle_id_and_file_name_unique" UNIQUE("particle_id", "file_name")	
);

CREATE TABLE "Nanoparticles" (
  "formulation_id" Varchar,
  "solid_fraction" Varchar,
  PRIMARY KEY ("formulation_id")
);

CREATE TABLE "MPT videos" (
  "video_id" Varchar,
  "formulation_id" Varchar,
  "sample_id" Varchar,
  PRIMARY KEY ("video_id"),
  CONSTRAINT "FK_MPT videos.formulation_id"
    FOREIGN KEY ("formulation_id")
      REFERENCES "Nanoparticles"("formulation_id")
);

CREATE TABLE "Confocal Parameters" (
  "file_name" Varchar,
  "formulation_id" Varchar,
  "sample_id" Integer,
  PRIMARY KEY ("file_name"),
  CONSTRAINT "FK_Confocal Parameters.sample_id"
    FOREIGN KEY ("sample_id")
      REFERENCES "Biological Sample Info"("Sample_ID")
);

