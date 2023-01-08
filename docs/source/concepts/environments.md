# Environments

## Rigid-body

### Pick-and-Place

#### PickCube-v0

Pick a cube up and move it to a goal position.

#### StackCube-v0

Place a red cube onto a green one

#### PickSingleYCB-v0

Pick a YCB object up and move it to a goal position.

Use all models:

```python
env = gym.make("PickSingleYCB-v0")
```

Use a single model:

```python
env = gym.make("PickSingleYCB-v0", model_ids="002_master_chef_can")
```

Use multiple models:

```python
env = gym.make("PickSingleYCB-v0", model_ids=["002_master_chef_can", "003_cracker_box"])
```

Model ids can be found in `mani_skill2/assets/mani_skill2_ycb/info_pick_v0.json`.

#### PickSingleEGAD-v0

Pick an EGAD object up and move it to a goal position.

You can use a similar way as `PickSingleYCB` to select models. Model ids can be found in `mani_skill2/assets/mani_skill2_egad/info_pick_train_v0.json`.

#### PickClutterYCB-v0

Pick a YCB object up and move it to a goal position. There are multiple objects in the scene. The target object is specified by a visible 3D point on its surface.

### Assembly

#### PegInsertionSide-v0

Insert a peg into a box with a hole (horizontally).

#### PlugCharger-v0

Plug a charger into a receptacle (horizontally).

#### AssemblingKits

Insert an object into its slot on the board.

### Miscellaneous

#### PandaAvoidObstacles-v0

Move the end-effector of Panda to reach a goal pose. There are obstacles in the scene.

#### TurnFaucet-v0

Use all models:

```python
env = gym.make("TurnFaucet-v0")
```

Use a single model:

```python
env = gym.make("TurnFaucet-v0", model_ids="5000")
```

Use multiple models:

```python
env = gym.make("TurnFaucet-v0", model_ids=["5001", "5002"])
```

Model ids can be found in `mani_skill2/assets/partnet_mobility/meta/info_faucet_train.json`.

### Mobile Manipulation from ManiSkill1

#### OpenCabinetDoor-v1

Control a single-arm mobile manipulator to open the cabinet door to some extent. There can be multiple doors of the cabinet. The target door is specified by the link (center of mass) position, and the desired direction to rotate is specified by the joint axis.

#### OpenCabinetDrawer-v1

Control a single-arm mobile manipulator to open the cabinet drawer to some extent. There can be multiple drawers of the cabinet. The target door is specified by (center of mass), and the desired direction to translate is specified by the joint axis.

#### PushChair-v1

Control a dual-arm mobile manipulator to push the chair to goal.

#### MoveBucket-v1

Control a dual-arm mobile manipulator to move the bucket onto a goal platform.

## Soft-body

### Excavate-v0

Lift a number of particles to a specific height.

Initial state:

* Random bucket position & rotation
* Random heightmap

Success metric:

* The number of lifted particles within a given range
* The lifted particles are higher than h
* Spilled particles < 20
* Particles velocity < 0.05

### Fill-v0

Fill particles from a bucket into the target beaker.

Initial state:

* Random bucket rotation
* Random beaker position

Success metric:

* The number of particles inside the target beaker is > 90%
* Particles velocity < 0.05

### Pour-v0

Pour water from a bottle into the target beaker.

Initial state:

* Random bottle position (gripper holds the bottle)
* Random water level within the bottle
* Random beaker position

Success metric:

* The water level in the target beaker reaches the red line
* Spill particles < 100
* Bottle keeps upright
* Robot arm velocity < 0.05

### Hang-v0

Hang a noodle on the rod.

Initial state:

* Random gripper position
* Random rod position & rotation

Success metric:

* Part of the noodle higher than the rod
* Two ends of the noodle are on different sides of the rod
* The noodle is not touching the ground
* The gripper is open
* Particles velocity < 0.05

### Write-v0

Write the target pattern using a stick.

### Pinch-v0

Pinch plasticine into a target shape.
