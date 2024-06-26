-- # Class: "WorkflowExecutionActivityCollection" Description: "A holder for Activity objects"
--     * Slot: id Description: 
-- # Class: "WorkflowExecutionActivity" Description: ""
--     * Slot: id Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: was_informed_by Description: 
--     * Slot: WorkflowExecutionActivityCollection_id Description: Autocreated FK slot
-- # Class: "Activity" Description: "Something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities."
--     * Slot: id Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
--     * Slot: was_informed_by Description: 
-- # Class: "OmicsProcessing" Description: ""
--     * Slot: id Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
-- # Class: "PlannedProcess" Description: ""
--     * Slot: id Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
-- # Class: "NamedThing" Description: "a databased entity or concept/class"
--     * Slot: id Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI

CREATE TABLE "WorkflowExecutionActivityCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Activity" (
	id TEXT NOT NULL, 
	was_informed_by TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id)
);
CREATE TABLE "OmicsProcessing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "PlannedProcess" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "WorkflowExecutionActivity" (
	id TEXT NOT NULL, 
	was_informed_by TEXT, 
	"WorkflowExecutionActivityCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(was_informed_by) REFERENCES "Activity" (id), 
	FOREIGN KEY("WorkflowExecutionActivityCollection_id") REFERENCES "WorkflowExecutionActivityCollection" (id)
);